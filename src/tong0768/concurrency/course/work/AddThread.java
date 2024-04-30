package tong0768.concurrency.course.work;

public class AddThread extends Thread {

    private final Warehouse warehouse;

    public AddThread(Warehouse warehouse) {
        this.warehouse = warehouse;
    }

    @Override
    public void run() {
        warehouse.add();
    }
}
