import { useState } from 'react';
import axios from 'axios';
import './source/stylesheets/form.css';

function App() {

  // const [reviews, setReviews] = useState([]);
  const [name, setName] = useState([]);
  const [anamnesis, setAnamnesis] = useState([]);
  const [diagnosis, setDiagnosis] = useState([]);

  // useEffect(() => {
  //   axios.get('http://localhost:8000/api/reviews/')
  //     .then(({ data }) => {
  //       console.log(data)
  //       setReviews(() => {
  //         return data
  //       })
  //     })
  //     .catch(error => {
  //       console.log(error);
  //     })
  // }, [])

  // Send data to the server
  const sendData = (e) => {

    e.preventDefault();

    axios.post('http://localhost:8000/api/review/', {name:anamnesis})
    .then((response) => {
      console.log(response.data);
      setDiagnosis(name+" tiene "+response.data.texto_mod);
    })
    .catch((error) => {
      console.log(error);
    })
  }

  // Return the JSX
  return (
    <div className="form_container">
      {/* Input data form */}
      <form action="" onSubmit={sendData}>

        <h2>Información del paciente</h2>
        {/* Nombre del paciente */}
        <div className='form-group'>
          <label htmlFor="">Nombre del paciente</label>
          <input
            className='form-control' 
            type="text"
            placeholder='Tobbie' 
            onChange={e => setName(e.target.value)}/>
        </div>

        {/* Anamnesis */}
        <div className='form-group'>
          <label htmlFor="">Anemnesis</label>
          <textarea
            className='form-control'
            placeholder='El tutor informa de la presencia de lesiones eritematosas y costrosas en la zona lumbar y caderas.'
            name="" 
            id="" 
            onChange={e => setAnamnesis(e.target.value)}></textarea>
        </div>

        <button type='submit'> Generar Diagnostico </button>

        <div className='form-group'>
          <label>Posible Diagnostico</label>
          <textarea 
            className='form-control'
            name="diagnosis" 
            id="diagnosis" 
            readOnly 
            value={diagnosis}></textarea>
        </div>

      </form>
    </div>
  )
}

export default App
