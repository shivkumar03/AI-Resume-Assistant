import "./App.css";
import ResumeForm from "./components/ResumeForm";
import UploadAnalyzer from "./components/UploadAnalyzer";
import ATSScore from "./components/ATSScore";
import Dashboard from "./components/Dashboard";

function App() {
  return (
    <div className="container">
      <h1 style={{ textAlign: "center", marginBottom: "30px" }}>
        🤖 AI Resume & Interview Assistant
      </h1>

      <ResumeForm />
      <UploadAnalyzer />
      <ATSScore />
      <Dashboard />
    </div>
  );
}

export default App;