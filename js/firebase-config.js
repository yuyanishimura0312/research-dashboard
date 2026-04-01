// Firebase Configuration — shared with Future Insight Workspace (miratuku-afa2c)
const firebaseConfig = {
  apiKey: "AIzaSyB5ubJobtiCOelI-hI6vQ9cyMnBBewyNwg",
  authDomain: "miratuku-afa2c.firebaseapp.com",
  projectId: "miratuku-afa2c",
  storageBucket: "miratuku-afa2c.firebasestorage.app",
  messagingSenderId: "344400461535",
  appId: "1:344400461535:web:544ebe32ad4add42f4b36a",
  measurementId: "G-4RX7K7D04W"
};

firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.firestore();
