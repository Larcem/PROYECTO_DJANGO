import React, { useEffect, useRef } from 'react';
import { pdfjs } from 'pdfjs-dist';
import 'pdfjs-dist/build/pdf.css';
import './User.css';

import examplePdf from './Unsa_comedor.pdf';

pdfjs.GlobalWorkerOptions.workerSrc = `https://unpkg.com/pdfjs-dist@${pdfjs.version}/build/pdf.worker.min.js`;

function User() {
  const canvasRef = useRef(null);

  useEffect(() => {
    const loadPdf = async () => {
      try {
        const pdf = await pdfjs.getDocument(examplePdf).promise;
        const page = await pdf.getPage(1);
        const viewport = page.getViewport({ scale: 1 });

        const canvas = canvasRef.current;
        const context = canvas.getContext('2d');
        canvas.height = viewport.height;
        canvas.width = viewport.width;

        const renderContext = {
          canvasContext: context,
          viewport,
        };
        await page.render(renderContext).promise;
      } catch (error) {
        console.error('Error loading PDF:', error);
      }
    };

    loadPdf();
  }, []);

  return (
    <div className="user-container">
      <canvas ref={canvasRef}></canvas>
    </div>
  );
}

export default User;
