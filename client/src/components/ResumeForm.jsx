import { useState } from "react";

function ResumeForm() {
  const [content, setContent] = useState("");

  const generateResume = async () => {
    const res = await fetch("http://localhost:5000/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ content })
    });

    const data = await res.json();

    if (data.message) {
      alert("Resume Generated ✅");
    } else {
      alert("Error generating resume");
    }
  };

  const downloadPDF = () => {
    window.open("http://localhost:5000/download");
  };

  return (
    <div className="card">
      <h2>AI Resume Generator</h2>

      <textarea
        placeholder="Write your resume content..."
        value={content}
        onChange={(e) => setContent(e.target.value)}
      />

      <button onClick={generateResume}>Generate Resume</button>
      <button onClick={downloadPDF}>Download PDF</button>
    </div>
  );
}

export default ResumeForm;