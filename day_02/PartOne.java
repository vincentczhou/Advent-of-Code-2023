package org.adventofcode2023;

import lombok.SneakyThrows;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;

public class PartOne {

    public static Map<String, Integer> limits = new HashMap<>() {{
        put("red", 12);
        put("green", 13);
        put("blue", 14);
    }};

    public static int parseLine(String line) {
        String[] chunk = line.split(":");
        int id = Integer.parseInt(chunk[0].split(" ")[chunk[0].split(" ").length - 1]);
        String[] cubeSets = chunk[1].split(";");

        for (String set : cubeSets) {
            String[] colorSets = set.split(",");
            for (String colorSet : colorSets) {
                String[] numColorCube = colorSet.trim().split(" ");
                int num = Integer.parseInt(numColorCube[0]);
                String color = numColorCube[1];
                if (num > limits.get(color)) {
                    id = 0;
                }
            }
        }

        return id;

    }

    public static void main(String[] args) {
        var input = getInput("input");

        int sum = 0;
        String[] inputLines = input.split("\n");
        for (String line : inputLines) {
            sum += parseLine(line);
        }

        System.out.printf("The sum is: %s", sum);
    }

    @SneakyThrows
    @SuppressWarnings({"SameParameterValue", "DataFlowIssue"})
    private static String getInput(String fileName) {
        return Files.readString(Paths.get(Main.class.getClassLoader().getResource(fileName).toURI())).trim();
    }
}