import { useState } from "react";

function ATSScore() {
  const [resume, setResume] = useState("");
  const [job, setJob] = useState("");
  const [score, setScore] = useState(null);
  const [keywords, setKeywords] = useState([]);

  const checkATS = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/ats-score", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          resume: resume,
          job: job
        })
      });

      const data = await response.json();

      if (response.ok) {
        setScore(data.score);
        setKeywords(data.matched_keywords);
      } else {
        alert(data.error || "Error checking ATS score");
      }

    } catch (error) {
      console.error(error);
      alert("Backend not running or wrong URL");
    }
  };

  return (
    <div className="card">
      <h2>ATS Score Checker</h2>

      <textarea
        placeholder="Paste Resume Text"
        value={resume}
        onChange={(e) => setResume(e.target.value)}
      />

      <textarea
        placeholder="Paste Job Description"
        value={job}
        onChange={(e) => setJob(e.target.value)}
      />

      <button onClick={checkATS}>Check ATS Score</button>

      {score !== null && (
        <div style={{ marginTop: "20px" }}>
          <h3>ATS Score: {score}%</h3>
          <p>Matched Keywords:</p>
          <ul>
            {keywords.map((word, index) => (
              <li key={index}>{word}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default ATSScore;