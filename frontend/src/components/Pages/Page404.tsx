import { WarningTwoIcon } from "@chakra-ui/icons";
import { Box, Heading, Icon, Text } from "@chakra-ui/react";

const Page404 = () => (
  <Box
    height="100vh"
    display="flex"
    flexDirection="column"
    alignItems="center"
    justifyContent="center"
    bg="gray.100"
    textAlign="center"
    px={4}
  >
    <Icon as={WarningTwoIcon} boxSize={24} color="brand.500" />
    <Heading fontSize="m" fontWeight="bold" textTransform="uppercase" color="brand.500">
      Page Not Found
    </Heading>
    <Box>
      <Text size="m" color="gray.500">
        Sorry, this page no longer exists
      </Text>
    </Box>
  </Box>
);

export default Page404;
