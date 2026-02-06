import { useState } from "react";

function App() {
  const [area, setArea] = useState("");
  const [bedrooms, setBedrooms] = useState("");
  const [result, setResult] = useState(null);

  const predict = async () => {
    const res = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        area: Number(area),
        bedrooms: Number(bedrooms),
      }),
    });

    const data = await res.json();
    setResult(data.predicted_price);
  };

  return (
    <div style={{ padding: "40px" }}>
      <h2>🏠 House Price Predictor</h2>

      <input placeholder="Area" onChange={e => setArea(e.target.value)} />
      <br /><br />
      <input placeholder="Bedrooms" onChange={e => setBedrooms(e.target.value)} />
      <br /><br />

      <button onClick={predict}>Predict</button>

      {result && <h3>Predicted Price: {result} lakhs</h3>}
    </div>
  );
}

export default App;
