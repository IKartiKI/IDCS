import React from "react";
import { Box } from "@mui/material";

const StartClass = () => {
  return (
    <Box border={"1px solid red"} display={"flex"} gap={"10px"}>
      <Box
        sx={{
          backgroundColor: "black",
          height: "100vh",
          width: "70%",
        }}
      ></Box>
      <Box display={"flex"} flexDirection={"column"} width={"30%"} gap={"10px"}>
        <Box
          sx={{
            backgroundColor: "black",
            height: "49vh",
          }}
        ></Box>
        <Box
          sx={{
            backgroundColor: "black",
            height: "49vh",
          }}
        ></Box>
      </Box>
    </Box>
  );
};

export default StartClass;
