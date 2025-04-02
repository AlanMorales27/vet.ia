import { createRoot } from 'react-dom/client'
import App from './assets/App.jsx'
import { AnamnesisForm } from './assets/source/pages/veterinaryConsultation/anamnesis/anamnesis.tsx'

createRoot(document.getElementById('root')).render(
     <AnamnesisForm />
)
