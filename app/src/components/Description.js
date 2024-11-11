import { useQuiz } from "../contexts/QuizContext";

function Description() {
  const { questions, index } = useQuiz();

  // Assuming each question is an object and the rich text is stored in a `description` field
  const questionDescription = questions.at(index)?.description || "";

  return <div dangerouslySetInnerHTML={{ __html: questionDescription }} />;
}

export default Description;
