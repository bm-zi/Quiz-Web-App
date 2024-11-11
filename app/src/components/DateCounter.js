// step 09
import { useReducer } from "react";

// Step 16
const initialState = { count: 0, step: 1 };

function reducer(state, action) {
  // step 08
  console.log(state, action);

  // step 10
  // return { count: 0, step: 1 };

  // step 11
  // switch (action.type) {
  //   case "dec":
  //     return { ...state, count: state.count - 1 };
  //   case "inc":
  //     return { ...state, count: state.count + 1 };
  //   case "setCount":
  //     return { ...state, count: action.payload };

  //   default:
  //     throw new Error("Unkown action");
  // }

  // step 13
  // switch (action.type) {
  //   case "dec":
  //     return { ...state, count: state.count - state.step };
  //   case "inc":
  //     return { ...state, count: state.count + state.step };
  //   case "setCount":
  //     return { ...state, count: action.payload };
  //   case "setStep":
  //     return { ...state, step: action.payload };
  //   default:
  //     throw new Error("Unkown action");
  // }

  // step 15
  switch (action.type) {
    case "dec":
      return { ...state, count: state.count - state.step };
    case "inc":
      return { ...state, count: state.count + state.step };
    case "setCount":
      return { ...state, count: action.payload };
    case "setStep":
      return { ...state, step: action.payload };
    case "reset":
      // return { count: 0, step: 1 };
      return initialState;

    default:
      throw new Error("Unkown action");
  }

  // step 07
  // if (action.type === "inc") return state + 1;
  // if (action.type === "dec") return state - 1;
  // if (action.type === "setCount") return action.payload;
}

function DateCounter() {
  // step 01
  // const [step, setStep] = useState(1);

  // step 02
  // const initialState = { count: 0, step: 1 };

  // step 03
  const [state, dispatch] = useReducer(reducer, initialState);

  // step 04
  const { count, step } = state;

  const date = new Date("april 18 2024");
  date.setDate(date.getDate() + count);

  const dec = function () {
    dispatch({ type: "dec" });
  };

  const inc = function () {
    dispatch({ type: "inc" });
  };

  const defineCount = function (e) {
    dispatch({ type: "setCount", payload: Number(e.target.value) });
  };

  const defineStep = function (e) {
    // step 12
    dispatch({ type: "setStep", payload: Number(e.target.value) });

    // step 05
    // setStep(Number(e.target.value));
  };

  const reset = function () {
    // step 14
    dispatch({ type: "reset" });

    // step 06
    // setStep(1);
  };

  return (
    <div className="counter">
      <div>
        <input
          type="range"
          min="0"
          max="10"
          value={step}
          onChange={defineStep}
        />
        <span>{step}</span>
      </div>

      <div>
        <button onClick={dec}>-</button>
        <input value={count} onChange={defineCount} />
        <button onClick={inc}>+</button>
      </div>

      <p>{date.toDateString()}</p>

      <div>
        <button onClick={reset}>Reset</button>
      </div>
    </div>
  );
}
export default DateCounter;

// Total steps = 16
