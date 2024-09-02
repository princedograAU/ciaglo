import { Button, Flex, Text, Menu, MenuButton, MenuItem, MenuList } from "@chakra-ui/react";
import { LuSettings2 } from "react-icons/lu";

const SearchFilters = () => (
  <Flex gap="2">
    <Menu>
      <MenuButton variant="outline" as={Button} leftIcon={<LuSettings2 />}>
        Filters
      </MenuButton>
      <MenuList>
        <MenuItem>
          <Text size="s">Property Type</Text>
        </MenuItem>
      </MenuList>
    </Menu>
  </Flex>
);

export default SearchFilters;
