import { extendTheme } from '@chakra-ui/react';

const theme = extendTheme({
  colors: {
    brand: {
      50: "#e2f2f3",
      100: "#b6dfe1",
      200: "#88cbcd",
      300: "#5cb7b8",
      400: "#40a7a7",
      500: "#319795",
      600: "#2d8a88",
      700: "#2a7a77",
      800: "#286a66",
      900: "#224d49",
      secondary: '#023047',
    },
  },
  fonts: {
    heading: `'Lato', sans-serif`,
    body: `'Lato', sans-serif`,
  },
  components: {
    Button: {
      variants: {
        solid: {
          bg: 'brand.400',
          color: 'white',
          fontWeight: '700',
          _hover: {
            bg: 'brand.600',
          },
          _active: {
            bg: 'brand.600'
          }
        },
      },
    },
    Link: {
      baseStyle: {
        color: 'brand.primary',
        _hover: {
          color: 'brand.secondary',
        },
      },
    },
  },
  config: {
    initialColorMode: 'light',
    useSystemColorMode: false,
  },
});

export default theme;
