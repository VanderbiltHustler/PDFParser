import React from 'react';
import PDFUploader from './components/PDFUploader';

function App() {
  return (
    <div className="upload-container">
      <h1 style={{fontWeight: 'bold', lineHeight: '1.1em'}}>
        Welcome to <span className="gold-text">The Vanderbilt Hustler's</span> PDF Parser
      </h1>
      <p style={{justifyContent: 'center'}}>
        Simply upload your PDF and get a structured CSV in return! <br />
        <span style={{ fontStyle: 'italic' }}>
          For questions, comments, or curiosities, Slack the #data team
        </span>
      </p>

      <PDFUploader />

      <div className="hustler-logo" style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '10px' }}>
        <img src="/vhlogo.png" alt="Vanderbilt Hustler Logo" style={{ width: '50px', height: 'auto' }}/>
      </div>
      <div className="footer">
        PDF Parser App by 
          Katherine Oung and Sean Onamade
      </div>
    </div>
  );
}

export default App;
