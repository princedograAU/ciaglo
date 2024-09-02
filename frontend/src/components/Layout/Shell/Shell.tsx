import { FC, ReactNode } from "react";
import Navbar from "../Navbar/Navbar";
import Footer from "../Footer/Footer";
import { Box } from "@chakra-ui/react";

interface ShellProps {
  children: ReactNode;
}

const Shell: FC<ShellProps> = ({ children }) => (
  <>
    <Navbar />
    <Box minH="100vh" margin="0 auto" maxW="8xl">
      {children}
    </Box>
    <Footer />
  </>
);

export default Shell;
