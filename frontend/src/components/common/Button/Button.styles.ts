import styled, { css } from 'styled-components';
import { ButtonVariant } from './Button';
import { ButtonProps } from 'react-bootstrap';
import { darken, lighten } from 'polished';

export const StyledButton = styled.button<ButtonProps>`
  padding: 6px 12px;
  border-radius: 4px;
  font-weight: 700;
  font-size: 16px;
  line-height: 24px;
  cursor: pointer;
  text-transform: capitalise;
  transition: background-color 0.3s ease;

  ${({ variant }) => variant === ButtonVariant.FILLED && css`
      background-color: ${props => props.theme.colors.primary};
      color: ${props => props.theme.colors.light};
      border: none;

      &:hover {
        background-color: ${props => darken(0.1, props.theme.colors.primary)};
      }

      &:active {
        background-color: ${props => props.theme.colors.primary};
      }

      &:disabled {
        background-color: ${props => props.theme.colors.dark};
        cursor: not-allowed;
      }
    `}

  ${({ variant }) =>
    variant === ButtonVariant.OUTLINED &&
    css`
      background-color: transparent;
      color: ${props => props.theme.colors.primary};
      border: 2px solid ${props => props.theme.colors.primary};

      &:hover {
        background-color: ${props => props.theme.colors.primary};
        color: ${props => props.theme.colors.light};
      }

      &:active {
        background-color: ${props => props.theme.colors.primary}s;
      }

      &:disabled {
        color: ${props => props.theme.colors.dark};
        border-color: ${props => props.theme.colors.dark};
        cursor: not-allowed;
      }
    `}

  ${({ variant }) =>
    variant === ButtonVariant.TEXT &&
    css`
      background-color: transparent;
      color: ${props => props.theme.colors.primary};
      border: none;

      &:hover {
        background-color: ${props => lighten(0.5, props.theme.colors.primary)};
      }

      &:active {
        color: ${props => props.theme.colors.primary};
        background-color: ${props => lighten(0.5, props.theme.colors.primary)};
      }

      &:disabled {
        color: ${props => props.theme.colors.dark};
        cursor: not-allowed;
      }
    `}
`;