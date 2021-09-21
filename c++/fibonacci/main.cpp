#include <iostream>

using namespace std;

int main()
{
    // SERIE FIBONACCI
    // [0] [1] [1] [2] [3] [5] [8]

    unsigned long long aux = 1, fibonacci = 0, lim, init;
    bool cerrar = true;

    while (cerrar) {
        cout << "Ingresa un numero para hacer la serie fibonacci: ";
        cin >> lim;

        if (lim > 0) {
            for (init = 1; init <= lim; init++) {
                cout << "[" << fibonacci << "] ";
                aux += fibonacci;
                fibonacci = aux - fibonacci;
            }
        } else {
            cout << "En numero debe ser mayor a 0" << endl;
            main();
        }

        cout << "\n" << endl;

        cout << "¿Deseas hacer otra serie? 1: SI / 0: NO ";
        cin >> cerrar;
        cout << "---------------------------";
        cout << "\n" << endl;
    }

    return 0;
}
