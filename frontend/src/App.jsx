import { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const uploadPDF = async () => {
    if (!file) {
      alert("Please select a PDF");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/upload",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      setMessage(data.message);
      console.log(data);
    } catch (error) {
      console.error(error);
      setMessage("Upload failed");
    }
  };

  return (
    <div>
      <h1>AI Powered PDF Summarizer</h1>
      <input type="file" accept=".pdf" onChange={(e) => setFile(e.target.files[0])}/>
      <input type = "text"/>
      <button className="upload-btn" onClick={uploadPDF}>Upload PDF</button>
      <button>hii</button>
      <p>{message}</p>
    </div>
  );
}

export default App;