package org.adventofcode2023;

import lombok.SneakyThrows;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class PartTwo {

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

    private static void clearVisit(Node[][] grid) {
        for (Node[] line : grid) {
            for (Node n : line) {
                n.visited = false;
            }
        }
    }

    private static int fill(int row, int col, int steps, Node[][] grid, Map<String, Integer> m) {
        int num = search(row, col, steps, grid, m);
        clearVisit(grid);
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

        int iSteps = 26501365; // Starting node is included in search
        int size = grid.length;
        assert size % 2 == 1;
        assert size == grid[0].length;
        assert start.row == start.col;
        assert start.row == size / 2;
        assert iSteps % size == size / 2;

        int inGridWidth = (iSteps / grid.length) - 1;
        double odd = Math.pow((inGridWidth / 2 * 2) + 1, 2);
        double even = Math.pow((inGridWidth + 1) / 2 * 2, 2);

        int oddPoints = fill(start.row, start.col, (size * 2 + 1) + 1, grid, new HashMap<>());
        int evenPoints = fill(start.row, start.col, (size * 2 + 1), grid, new HashMap<>());

        int tCorner = fill(size - 1, start.col, (size - 1) + 1, grid, new HashMap<>());
        int rCorner = fill(start.row, 0, (size - 1) + 1, grid, new HashMap<>());
        int bCorner = fill(0, start.col, (size - 1) + 1, grid, new HashMap<>());
        int lCorner = fill(start.row, size - 1, (size - 1) + 1, grid, new HashMap<>());

        int trSmall = fill(size - 1, 0, (size / 2 - 1) + 1, grid, new HashMap<>());
        int tlSmall = fill(size - 1, size - 1, (size / 2 - 1) + 1, grid, new HashMap<>());
        int brSmall = fill(0, 0, (size / 2 - 1) + 1, grid, new HashMap<>());
        int blSmall = fill(0, size - 1, (size / 2 - 1) + 1, grid, new HashMap<>());

        int trLarge = fill(size - 1, 0, (size * 3 / 2 - 1) + 1, grid, new HashMap<>());
        int tlLarge = fill(size - 1, size - 1, (size * 3 / 2 - 1) + 1, grid, new HashMap<>());
        int brLarge = fill(0, 0, (size * 3 / 2 - 1) + 1, grid, new HashMap<>());
        int blLarge = fill(0, size - 1, (size * 3 / 2 - 1) + 1, grid, new HashMap<>());

        long total = ((long) odd *  (long) oddPoints) + ((long) even * (long) evenPoints) + (long) tCorner + (long) rCorner + (long) bCorner + (long) lCorner + (((long) inGridWidth + 1) * ((long) trSmall + (long) tlSmall + (long) brSmall + (long) blSmall)) + (((long) inGridWidth) * ((long) trLarge + (long) tlLarge + (long) brLarge + (long) blLarge));

        System.out.printf("The total is: %s", total);
    }

    @SneakyThrows
    @SuppressWarnings({"SameParameterValue", "DataFlowIssue"})
    private static String getInput(String fileName) {
        return Files.readString(Paths.get(Main.class.getClassLoader().getResource(fileName).toURI())).trim();
    }
}