package tong0768.operation.scc211.concurrency.basic;

public class Main {

    // 主线程 竞争CPU
    public static void main(String[] args) {
        new AThread().start();

        int j = 0;
        while (true) {
            System.out.println("main: " + j++);
        }
    }

}
