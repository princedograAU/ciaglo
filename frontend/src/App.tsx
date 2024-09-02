import React from "react";
import { ChakraProvider } from "@chakra-ui/react";
import theme from "./theme";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Pages/Home";
import Page404 from "./components/Pages/Page404";

const App: React.FC = () => {
  return (
    <ChakraProvider theme={theme}>
      <Router>
        <Routes>
          <Route path="/" Component={Home} />
          <Route path="*" Component={Page404} />
        </Routes>
      </Router>
    </ChakraProvider>
  );
};

export default App;
