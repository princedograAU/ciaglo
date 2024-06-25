import 'styled-components';

declare module 'styled-components' {
  export interface DefaultTheme {
    colors: {
      primary: string;
      secondary: string;
      success: string;
      info: string;
      warning: string;
      danger: string;
      light: string;
      dark: string;
    };
  }
}
