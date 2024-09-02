import { LuAtSign } from "react-icons/lu";
import { Box, Button, Flex, Heading, Icon } from "@chakra-ui/react";
import SearchBar from "./SearchBar";
import { useNavigate } from "react-router-dom";
import SearchFilters from "./SearchFilters";
import { FaRegUserCircle } from "react-icons/fa";

const Navbar = () => {
  const navigate = useNavigate();
  return (
    <Box boxShadow="0px 1px 8px rgba(0, 0, 0, 0.1)">
      <Flex alignItems="center" gap="4" px="4" justifyContent="" margin="0 auto" maxW="8xl">
        <Flex
          borderRadius="5"
          backgroundColor="brand.700"
          p="2"
          cursor="pointer"
          onClick={() => navigate("/")}
        >
          <Icon as={LuAtSign} color="white" />
          <Heading size="md" color="white" textShadow={1}>
            CIAGLO
          </Heading>
        </Flex>
        <SearchBar />
        <SearchFilters />

        <Button
          color="brand.700"
          leftIcon={<FaRegUserCircle />}
          variant="outline"
          marginLeft="auto"
        >
          Log In
        </Button>
      </Flex>
    </Box>
  );
};

export default Navbar;
