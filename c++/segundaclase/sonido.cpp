#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    // caLCULADORA
    int numero1 = 0;
    int numero2 = 0;
    int opcion = 0;
    bool activarCalculadora = true;
    // Console out: COUT
    cout << "Introduce el primer numero: ";
    // Console in: CIN
    cin >> numero1;

    cout << "Introduce el segundo numero: ";
    cin >> numero2;

    do {
        cout << "\n Dime ¿Que quieres hacer?" << endl;
        cout << "1. Sumar" << endl;
        cout << "2. Restar" << endl;
        cout << "3. Dividir" << endl;
        cout << "4. Multiplicar" << endl;
        cout << "5. Raiz cuadrada" << endl;
        cout << "6. Potencia" << endl;
        cout << "7. Cambiar los valores" << endl;
        cout << "8. Salir" << endl;

        cout << "Elige una opcion: ";
        cin >> opcion;

        switch (opcion) {
            case 1:
                cout << "El resultado de la suma es: " << numero1 + numero2 << endl;
                break;
            case 2:
                cout << "El resultado de la resta es: " << numero1 - numero2 << endl;
                break;
            case 3:
                cout << "El resultado de la division es: " << numero1 / numero2 << endl;
                break;
            case 4:
                cout << "El resultado de la multiplicacion es: " << numero1 * numero2 << endl;
                break;
            case 5:
                cout << "El resultado de la raiz cuadrada es: " << sqrt(numero1) << endl;
                break;
            case 6:
                cout << "El resultado de la potencia es: " << pow(numero1, numero2) << endl;
                break;
            case 7:
                cout << "Introduce el primer numero: ";
                cin >> numero1;

                cout << "Introduce el segundo numero: ";
                cin >> numero2;
                break;
            case 8:
                activarCalculadora = false;
                break;
            default:
                cout << "Mete un valor correcto" << endl;
                break;
        }


    } while (activarCalculadora);

    cout << "Adios" << endl;

    return 0;

}

