import { Box, Flex, Heading, Icon } from "@chakra-ui/react";
import { LuAtSign } from "react-icons/lu";

const Footer = () => (
  <Box boxShadow="0px -1px 8px rgba(0, 0, 0, 0.1)" minH="250" backgroundColor="brand.secondary">
    <Box backgroundColor="brand.500" py="4">
      <Flex alignItems="center" gap="4" px="4" justifyContent="" margin="0 auto" maxW="8xl">
        <Flex borderRadius="5" p="2">
          <Icon as={LuAtSign} color="white" />
          <Heading size="md" color="white" textShadow={1}>
            CIAGLO
          </Heading>
        </Flex>
      </Flex>
    </Box>
  </Box>
);

export default Footer;
