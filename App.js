import React, { useState } from "react";

function App() {
  const [input, setInput] = useState("");
  const [result, setResult] = useState([]);

  const runWorkflow = async () => {
    const res = await fetch("http://localhost:8001/run", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ input }),
    });

    const data = await res.json();
    setResult(data.result);
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>🚀 AutoFlow AI</h1>

      <textarea
        rows="4"
        cols="50"
        placeholder="Enter workflow..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />

      <br /><br />

      <button onClick={runWorkflow} style={{ padding: "10px" }}>
        Run Workflow
      </button>

      <hr />

      {result.map((step, i) => (
        <div key={i} style={{
          background: "#f5f5f5",
          padding: "10px",
          margin: "10px",
          borderRadius: "8px"
        }}>
          <h4>Step {i + 1}</h4>
          <p>{step.step}</p>
          <p>Result: {step.result}</p>
          <p>Status: {step.verified ? "✅ Done" : "❌ Failed"}</p>
        </div>
      ))}
    </div>
  );
}

export default App;