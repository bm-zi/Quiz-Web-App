import React, { useEffect, useState } from "react";
import { useQuiz } from "../contexts/QuizContext"; // Access the context
import { useNavigate } from "react-router-dom"; // Import useNavigate
import Header from "./Header";
import { Link } from "react-router-dom";

const QuizList = () => {
  const [quizzes, setQuizzes] = useState([]);
  const [selectedQuizLocal, setSelectedQuizLocal] = useState("");
  const { setSelectedQuiz } = useQuiz(); // Get setSelectedQuiz from context
  const navigate = useNavigate(); // Initialize navigate

  useEffect(() => {
    const fetchQuizzes = async () => {
      try {
        const response = await fetch("http://localhost:8000/api/quiznames/");
        const data = await response.json();
        console.log("Fetched Quizzes:", data); // Check the structure
        setQuizzes(data);
      } catch (error) {
        console.error("Error fetching quizzes:", error);
      }
    };

    fetchQuizzes();
  }, []);

  const handleSelectionChange = (event) => {
    setSelectedQuizLocal(event.target.value);
  };

  const handleSubmit = () => {
    if (selectedQuizLocal) {
      setSelectedQuiz(selectedQuizLocal); // Update quiz name in context
      navigate("/"); // Navigate to the home page (adjust the path as needed)
    }
  };

  return (
    <div className="app">
      <Header />

      {/* <UploadQuiz /> */}
      <UploadQuestions />

      <div className="quiz">
        <h2>Select a quiz :</h2>

        {/* Check if quizzes is an array and contains elements */}
        <ul>
          {quizzes.length > 0 ? (
            quizzes.map((quiz, index) => (
              <li key={index}>
                <label>
                  <input
                    type="radio"
                    value={quiz.name} // Access the name property directly
                    checked={selectedQuizLocal === quiz.name}
                    onChange={handleSelectionChange}
                  />
                  {quiz.name} {/* Display quiz name */}
                </label>
              </li>
            ))
          ) : (
            <p>No quizzes available</p>
          )}
        </ul>

        <button
          style={{ marginTop: 40 }}
          className="btn btn-ui"
          onClick={handleSubmit}
          disabled={!selectedQuizLocal}
        >
          Submit
        </button>
      </div>
    </div>
  );
};

// function UploadQuiz() {
//   return (
//     <Link to="http://127.0.0.1:8000/upload_quiz_json">
//       <button className="btn">Quiz upload</button>
//     </Link>
//   );
// }

function UploadQuestions() {
  return (
    <Link to="http://127.0.0.1:8000/upload_questions/">
      <button className="btn">Quiz upload</button>
    </Link>
  );
}

export default QuizList;
