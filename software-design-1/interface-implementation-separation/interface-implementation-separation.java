import java.util.HashMap;
import java.util.Map;
import java.sql.*;

interface Storage {
    void save(String value);
    String retrieve(int id);
}

class DbStorage implements Storage {
    private Map<Integer, String> storage = new HashMap<>();

    public DbStorage() {
        loadFromDb();
    }

    @Override
    public void save(String value) {
        int id = storage.size();
        storage.put(id, value);
        saveToDb(id, value);
    }

    @Override
    public String retrieve(int id) {
        return storage.get(id);
    }

    private Connection connect() throws SQLException {
        return DriverManager.getConnection(
            "jdbc:mysql://localhost:3306/mydb",
            "username",
            "password"
        );
    }

    private void loadFromDb() {
        try (Connection connection = connect()) {
            ResultSet result = connection
                .prepareStatement("SELECT Id, Value FROM TableName")
                .executeQuery();

            while (result.next()) {
                int id = result.getInt("Id");
                String value = result.getString("Value");
                storage.put(id, value);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private void saveToDb(int id, String value) {
        try (Connection connection = connect()) {
            connection.createStatement()
                .executeUpdate(String.format("INSERT TableName(Id, Value) VALUES (%d, %s)", id, value));
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
