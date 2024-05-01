package tong0768.scc211.concurrency.exam2023.q1;

public class Share {

    private int num = 0;

    public synchronized void add() {
        num++;
    }

    public int getNum() {
        return num;
    }

}
