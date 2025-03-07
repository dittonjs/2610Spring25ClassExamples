import express from 'express';
import fib, { loopingFib } from "./fib.js";

const app = express();
const PORT = 3000;

app.get("/", (req, res) => {
  console.log(fib(10))
  res.send("<h1>Hello, world!</h1>");
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
