import { Inter } from "next/font/google";
import { useEffect, useState } from "react";
import animalService from "@/services/animalService";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
  const [animals, setAnimals] = useState<Animal[]>();

  useEffect(() => {
    animalService.getAllAnimals().then((response) => setAnimals(response))
  }, [])


  return (
    <main>
      {animals?.map(animal => { 
        return (
          <section key={animal.id}>
          <h1>{animal.name}</h1>
          <h2>{animal.species}</h2>
          <h3>{animal.breed}</h3>
          <h3>{animal.age}</h3>
          </section>
        )
      })}
    </main>
  );
}
