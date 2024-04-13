// App.js
import React, { useState } from "react";

const StoT = () => {
  const [text, setText] = useState("");

  const handleAudioUpload = async (event) => {
    const file = event.target.files[0];
    const formData = new FormData();
    formData.append("audio", file);

    try {
      const response = await fetch("http://localhost:5000/speech-to-text", {
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      setText(data.text || data.error);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div>
      <input type="file" accept="audio/*" onChange={handleAudioUpload} />
      <p>{text}</p>
    </div>
  );
};

export default StoT;
