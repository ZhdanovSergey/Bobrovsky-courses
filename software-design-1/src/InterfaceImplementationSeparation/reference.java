package InterfaceImplementationSeparation;

import java.sql.*;

interface Storage {
    void save(String value);
    String retrieve(int id);
}

class DatabaseStorage implements Storage {
    private Connection connection;
    public DatabaseStorage(Connection connection) {
        this.connection = connection;
    }

    @Override
    public void save(String data) {
        try {
            PreparedStatement stmt = 
    connection.prepareStatement("INSERT INTO storage (data) VALUES (?)");
            stmt.setString(1, data);
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    @Override
    public String retrieve(int id) {
        try {
            PreparedStatement stmt = 
    connection.prepareStatement("SELECT data FROM storage WHERE id = ?");
            stmt.setInt(1, id);
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                return rs.getString("data");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }
}

class StorageTest {
    public static void main(String[] args) {
        try {
            Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "name", "pass");
            Storage databaseStorage = new DatabaseStorage(connection);
            testStorage(databaseStorage);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private static void testStorage(Storage storage) {
        storage.save("Hello, World!");
        storage.save("Second string");

        String data1 = storage.retrieve(0);
        String data2 = storage.retrieve(1);

        System.out.println("Retrieved data1: " + data1);
        // Retrieved data1: Hello, World!

        System.out.println("Retrieved data2: " + data2);
        // Retrieved data2: Second string
    }
}