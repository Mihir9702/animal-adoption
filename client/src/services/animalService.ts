import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000/api/animals/';


const animalService = {

  getAllAnimals: async () => {
    try {
      const response = await axios.get(BASE_URL);
      return response.data;
    } catch (error) {
      throw new Error('Failed to fetch animals');
    }
  },

};

export default animalService;
