import React, { useState } from "react";
import axios from "axios";
import "./styles.css";

function Predict() {
  const [input, setInput] = useState({
    bedrooms: 3,
    sqft: 1200,
    location: "urban"
  });
  const [price, setPrice] = useState(null);

  const handleChange = (e) => {
    setInput({ ...input, [e.target.name]: e.target.value });
  };

  const handlePredict = async () => {
    try {
      const res = await axios.post("http://localhost:8001/api/predict/", input);
      setPrice(res.data.predicted_price);
    } catch (err) {
      console.error(err);
      alert("Prediction failed.");
    }
  };

  return (
    <div className="form-page">
      <h2>Enter House Details</h2>
      <div className="form-group">
        <label>Bedrooms:</label>
        <input name="bedrooms" type="number" value={input.bedrooms} onChange={handleChange} />
      </div>
      <div className="form-group">
        <label>Square Feet:</label>
        <input name="sqft" type="number" value={input.sqft} onChange={handleChange} />
      </div>
      <div className="form-group">
        <label>Location:</label>
        <input name="location" type="text" value={input.location} onChange={handleChange} />
      </div>
      <button className="btn" onClick={handlePredict}>Predict Price</button>
      {price && <p className="result">💰 Predicted Price: ₹{price}</p>}
    </div>
  );
}

export default Predict;