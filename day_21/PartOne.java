package org.adventofcode2023;

import lombok.SneakyThrows;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

public class PartOne {

    private static class Node {
        public int row;
        public int col;
        public boolean visited;
        public char value;

        public Node(int row, int col, boolean visited, char value) {
            this.row = row;
            this.col = col;
            this.visited = visited;
            this.value = value;
        }

        public String toString() {
            return String.valueOf(this.value);
//            return String.format("row: %s col: %s visited: %s value: %s", this.row, this.col, this.visited, this.value);
        }
    }

    private static int search(int row, int col, int steps, Node[][] grid, Map<String, Integer> m) {
        if (row >= grid.length || row < 0 || col >= grid[0].length || col < 0) {
            return 0;
        } else if (steps == 0) {
            return 0;
        } else if (grid[row][col].value == '#') {
            return 0;
        }

        String k = String.format("row: %s col: %s steps: %s", row, col, steps);
        if (m.containsKey(k)) {
            return 0;
        }

        int num = 0;
        if (steps == 1 && !grid[row][col].visited) {
            num += 1;
            grid[row][col].visited = true;
        }

        int up = search(row - 1, col, steps - 1, grid, m);
        int down = search(row + 1, col, steps - 1, grid, m);
        int left = search(row, col - 1, steps - 1, grid, m);
        int right = search(row, col + 1, steps - 1, grid, m);
        num = num + up + down + left + right;

        m.put(k, num);

        return num;
    }

    public static <T> void printSection(T[][] section) {
        for (T[] line : section) {
            System.out.println(Arrays.toString(line));
        }
        System.out.println();
    }

    public static void main(String[] args) {
        var input = getInput("input");

        String[] inputLines = input.split("\n");
        Node[][] grid = new Node[inputLines.length][inputLines[0].length()];

        Node start = null;

        for (int i = 0; i < inputLines.length; i++) {
            for (int j = 0; j < inputLines[0].length(); j++) {
                Node curr = new Node(i, j, false, inputLines[i].charAt(j));
                if (inputLines[i].charAt(j) == 'S') {
                    start = curr;
                }
                grid[i][j] = curr;
            }
        }

        assert start != null;
        int steps = 64 + 1; // Starting node is included in search
        Map<String, Integer> m = new HashMap<>();
        int num = search(start.row, start.col, steps, grid, m);
        System.out.printf("The total is: %s", num);
    }

    @SneakyThrows
    @SuppressWarnings({"SameParameterValue", "DataFlowIssue"})
    private static String getInput(String fileName) {
        return Files.readString(Paths.get(Main.class.getClassLoader().getResource(fileName).toURI())).trim();
    }
}