const openCameraBtn = document.getElementById('openCameraBtn');
const video = document.getElementById('video');
const dizzinessScore = document.getElementById('dizzinessScore');

let stream = null;
let captureInterval = null;

// Function to open webcam
async function openCamera() {
  try {
    stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
    video.srcObject = stream;
    video.play();
    
    openCameraBtn.textContent = "Camera Opened";
    openCameraBtn.disabled = true;

    // Start sending frames to backend
    captureInterval = setInterval(sendFrame, 500); // every 500ms

  } catch (err) {
    alert("Error accessing camera: " + err);
  }
}

// Convert video frame to base64 JPEG
function getFrameBase64() {
  const canvas = document.createElement('canvas');
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  const ctx = canvas.getContext('2d');
  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
  return canvas.toDataURL('image/jpeg', 0.7); // 70% quality
}

// Send frame to backend
async function sendFrame() {
  if (!video.videoWidth) return;

  const dataUrl = getFrameBase64();

  try {
    const resp = await fetch('/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ image: dataUrl })
    });

    if (!resp.ok) throw new Error("Server error");

    const json = await resp.json();
    const val = Math.round(json.dizziness || 0);
    dizzinessScore.textContent = val + "%";

  } catch (err) {
    console.error("Error sending frame:", err);
  }
}

openCameraBtn.addEventListener('click', openCamera);