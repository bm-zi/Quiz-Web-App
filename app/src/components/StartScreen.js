import { useQuiz } from "../contexts/QuizContext";

function StartScreen() {
  const { numQuestions, dispatch, selectedQuiz, SECS_PER_QUESTION } = useQuiz();
  return (
    <div className="start">
      <h2>
        You selected quiz <span className="red">{selectedQuiz}</span> !
      </h2>
      <h3>
        Number of questions: <span className="red">{numQuestions}</span>
      </h3>
      <h3>
        Quiz time:{" "}
        <span className="red">{(numQuestions * SECS_PER_QUESTION) / 60}</span>{" "}
        min.
      </h3>
      <button
        className="btn btn-ui"
        onClick={() => dispatch({ type: "start" })}
      >
        Let's start
      </button>
    </div>
  );
}

export default StartScreen;
