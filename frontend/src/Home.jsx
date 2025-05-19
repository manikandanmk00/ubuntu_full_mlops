import React from "react";
import { Link } from "react-router-dom";
import "./styles.css";

function Home() {
  return (
    <div className="home-page">
      <h1>🏠 House Price Prediction</h1>
      <p>Welcome to the house price prediction tool. Click below to predict a price.</p>
      <Link to="/predict">
        <button className="btn">Go to Prediction</button>
      </Link>
    </div>
  );
}

export default Home;
