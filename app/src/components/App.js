import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Header from "./Header";
import Main from "./Main";
import Error from "./Error";
import Loader from "./Loader";
import StartScreen from "./StartScreen";
import Question from "./Question";
import NextButton from "./NextButton";
import Progress from "./Progress";
import FinishScreen from "./FinishScreen";
import Footer from "./Footer";
import Timer from "./Timer";
import { useQuiz } from "../contexts/QuizContext";
import QuizList from "./QuizList";

export default function App() {
  const { status } = useQuiz();

  return (
    <Router>
      <Routes>
        <Route
          path="/"
          element={
            <div className="app">
              <Header />

              <Main>
                {status === "loading" && <Loader />}
                {status === "error" && <Error />}
                {status === "ready" && <StartScreen />}
                {status === "active" && (
                  <>
                    <Progress />
                    <Question />
                    <Footer>
                      <Timer />
                      <NextButton />
                    </Footer>
                  </>
                )}
                {status === "finished" && <FinishScreen />}
              </Main>
            </div>
          }
        />
        <Route path="/quizzes" element={<QuizList />} />
      </Routes>
    </Router>
  );
}
