import React from 'react';
import { ThemeProvider } from 'styled-components';
import { theme } from './theme';
import Button from './components/common/Button/Button';


const App: React.FC = () => {
  return (
    <>
      <ThemeProvider theme={theme}>
        <h1>Welcome to Ciaglo</h1>
        <Button>Styled Button</Button>
      </ThemeProvider>
    </>
  );
};

export default App;