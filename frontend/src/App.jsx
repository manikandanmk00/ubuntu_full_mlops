import React, { useState } from "react";
import "./App.css";

const initialState = {
  OverallQual: 5,
  OverallCond: 5,
  TotRmsAbvGrd: 6,
  FullBath: 1,
  Fireplaces: 0,
  GrLivArea: 1500,
  TotalBsmtSF: 800,
  FirstFlrSF: 800,
  GarageArea: 300,
  BsmtFinSF1: 500,
  MasVnrArea: 0,
  LotArea: 7000,
  GarageCars: 1,
  YearBuilt: 2000,
  YearRemodAdd: 2010,
};

function App() {
  const [form, setForm] = useState(initialState);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm((prev) => ({
      ...prev,
      [name]: Number(value),
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setResult(null);
    setError("");

    try {
      const response = await fetch("http://localhost:8001/api/predict/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });

      const data = await response.json();

      if (response.ok) {
        setResult(data.predicted_price || JSON.stringify(data));
      } else {
        setError(data.detail || "Prediction failed.");
      }
    } catch (err) {
      setError("Server error: " + err.message);
    }
  };

  return (
    <div className="container">
      <h1>🏠 House Price Prediction</h1>
      <form onSubmit={handleSubmit}>
        <fieldset>
          <legend>🏡 Structure</legend>
          <Input label="Overall Quality" name="OverallQual" value={form.OverallQual} onChange={handleChange} />
          <Input label="Overall Condition" name="OverallCond" value={form.OverallCond} onChange={handleChange} />
          <Input label="Rooms Above Ground" name="TotRmsAbvGrd" value={form.TotRmsAbvGrd} onChange={handleChange} />
          <Input label="Full Bathrooms" name="FullBath" value={form.FullBath} onChange={handleChange} />
          <Input label="Fireplaces" name="Fireplaces" value={form.Fireplaces} onChange={handleChange} />
        </fieldset>

        <fieldset>
          <legend>📐 Size (sqft)</legend>
          <Input label="Above Ground Living Area" name="GrLivArea" value={form.GrLivArea} onChange={handleChange} />
          <Input label="Total Basement Area" name="TotalBsmtSF" value={form.TotalBsmtSF} onChange={handleChange} />
          <Input label="1st Floor Area" name="FirstFlrSF" value={form.FirstFlrSF} onChange={handleChange} />
          <Input label="Garage Area" name="GarageArea" value={form.GarageArea} onChange={handleChange} />
          <Input label="Finished Basement Area" name="BsmtFinSF1" value={form.BsmtFinSF1} onChange={handleChange} />
          <Input label="Masonry Veneer Area" name="MasVnrArea" value={form.MasVnrArea} onChange={handleChange} />
          <Input label="Lot Area" name="LotArea" value={form.LotArea} onChange={handleChange} />
        </fieldset>

        <fieldset>
          <legend>🚗 Garage</legend>
          <Input label="Garage Cars" name="GarageCars" value={form.GarageCars} onChange={handleChange} />
        </fieldset>

        <fieldset>
          <legend>📅 Year Built</legend>
          <Input label="Year Built" name="YearBuilt" value={form.YearBuilt} onChange={handleChange} />
          <Input label="Year Remodeled" name="YearRemodAdd" value={form.YearRemodAdd} onChange={handleChange} />
        </fieldset>

        <button type="submit">🔍 Predict</button>
      </form>

      {result && <div className="result">💰 Estimated Price: ${Number(result).toFixed(2)}</div>}
      {error && <div className="error">❌ {error}</div>}
    </div>
  );
}

const Input = ({ label, name, value, onChange }) => (
  <div className="form-group">
    <label htmlFor={name}>{label}</label>
    <input
      type="number"
      name={name}
      id={name}
      value={value}
      onChange={onChange}
      required
      min="0"
    />
  </div>
);

export default App;
