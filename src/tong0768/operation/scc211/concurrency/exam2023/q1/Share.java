package tong0768.operation.scc211.concurrency.exam2023.q1;

public class Share {

    private int num = 0;

    public synchronized void add() {
        num++;
        // temp = num + 1;
        // num = temp;
    }

    public int getNum() {
        return num;
    }

}
