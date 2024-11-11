import { useQuiz } from "../contexts/QuizContext";
import { Link, useLocation } from "react-router-dom";

function Header() {
  const { status } = useQuiz();
  const location = useLocation();
  return (
    <header className="app-header app">
      <Link to="/">
        <img src="multiple-choice.png" alt="Multiple Choice" />
      </Link>
      <h1>Quiz Collections</h1>

      {status === "ready" && location.pathname === "/" && <QuizLink />}
    </header>
  );
}

function QuizLink() {
  return (
    <Link to="/quizzes">
      <button className="btn" style={{ marginTop: 30 }}>
        Select Quiz
      </button>
    </Link>
  );
}

export default Header;
