import React, { useEffect } from "react";
import { useState } from "react";
import axios from "axios";

export const AnamnesisForm = () => {
  //! Store form data
  const [diagnosis, setDiagnosis] = useState();
  const [anamnesis, setAnamnesis] = useState({
    weight: 0,
    age: 0,
    vaccination: true,
    observation: "",
  });

  useEffect(() => {},[anamnesis]);

  const saveField = (e) => {
    setAnamnesis({
      ...anamnesis,
      [e.target.name]: e.target.type === "checkbox" 
      ? e.target.checked 
      : e.target.value});
  };

  function calAge() {}

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await axios.post("http://127.0.0.1:8000/", anamnesis);
      setDiagnosis(response.data.tensor_response);
      console.log(diagnosis);
      // Reset form
    } catch (error) {
      if (axios.isAxiosError(error)) {
        console.error(
          "Error en la solicitud",
          error.response?.data || error.message
        );
      } else {
        console.error("Error desconocido", error);
      }
    }
  };

  return (
    <>
      <form onSubmit={handleSubmit}>
        {/* Weight Field */}
        <div>
          <label htmlFor="weight">Peso</label>
          <input
            id="weight"
            type="number"
            name="weight"
            value={anamnesis.weight}
            onChange={saveField}
          />
        </div>
        {/* Age Field */}
        <div>
          <label htmlFor="age">Edad</label>
          <input
            id="age"
            type="number"
            name="age"
            value={anamnesis.age}
            onChange={saveField}
          />
        </div>
        {/* Vaccination field */}
        <div>
          <label htmlFor="vaccination">Vacunación al dia</label>
          <input
            id="vaccination"
            type="checkbox"
            name="vaccination"
            checked={anamnesis.vaccination}
            onChange={saveField}
          />
        </div>
        {/* Observation field */}
        <div>
          <label htmlFor="observation">Observaciones del propietario</label>
          <textarea
            name="observation"
            id="observation"
            value={anamnesis.observation}
            onChange={saveField}
          ></textarea>
        </div>
        <button type="submit">Submit</button>
      </form>
      <textarea disabled value={diagnosis}></textarea>
    </>
  );
};
