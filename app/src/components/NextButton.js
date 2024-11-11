import { useQuiz } from "../contexts/QuizContext";
import Description from "./Description";

function NextButton() {
  const { questions, dispatch, answer, index, numQuestions } = useQuiz();
  const questionDescription = questions.at(index)?.description || "";

  if (answer === null) return null;

  if (index < numQuestions - 1)
    return (
      <div>
        <button
          className="btn btn-ui"
          style={{ marginBottom: 20 }}
          onClick={() => dispatch({ type: "nextQuestion" })}
        >
          Next
        </button>
        <div className="description">
          {questionDescription !== "" && <h4>Description</h4>}
          <Description />
        </div>
      </div>
    );

  if (index === numQuestions - 1)
    return (
      <>
        <button
          className="btn btn-ui"
          onClick={() => dispatch({ type: "finish" })}
        >
          Finish
        </button>
        <div className="description">
          {questionDescription !== "" && <h4>Description</h4>}
          <Description />
        </div>
      </>
    );
}

export default NextButton;
