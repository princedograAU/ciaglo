import React, { ReactNode } from 'react';
import { StyledButton } from './Button.styles';

export enum ButtonVariant {
  OUTLINED = "outlined",
  FILLED = "filled",
  TEXT = "text"
}

export interface ButtonProps {
  // You can add any custom props if needed
  variant?: ButtonVariant;
  children: ReactNode
}

// Create the button component
const Button: React.FC<ButtonProps> = ({ children, variant, ...props }) => {
  return (
    <StyledButton
      variant={variant || ButtonVariant.FILLED}
      {...props}
    >
        {children}
    </StyledButton>);
};

export default Button;
