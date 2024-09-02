import { Flex, IconButton, Input, InputGroup, InputRightElement } from "@chakra-ui/react";
import { FaSearch } from "react-icons/fa";

const SearchBar = () => (
  <Flex flex="1" my={4} maxWidth="500">
    <InputGroup>
      <Input
        type="text"
        placeholder="Try a location you want to live by"
        focusBorderColor="teal.400"
        borderRadius="md"
        boxShadow="sm"
      />
      <InputRightElement>
        <IconButton
          aria-label="Search database"
          icon={<FaSearch color="brand.700" />}
          borderLeftRadius="none"
          borderRightRadius="md"
        />
      </InputRightElement>
    </InputGroup>
  </Flex>
);

export default SearchBar;
