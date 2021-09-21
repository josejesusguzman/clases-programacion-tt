#include <stdio.h>
#include <windows.h>

const char zClassName[] = "MiVentana";

int DisplayConfirmMessageBox()
{
    int msgBoxID = MessageBox(
        NULL,
        "Hola, me acabas de apretar. Que rico :3",
        "Aprietale :0",
        MB_ICONEXCLAMATION | MB_YESNO
    );

    if (msgBoxID == IDYES) {
        DisplayConfirmMessageBox();
    }

    return msgBoxID;
}

LRESULT CALLBACK WndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam)
{
    switch(msg) {
        case WM_CLOSE:
            DisplayConfirmMessageBox();
            DestroyWindow(hwnd);
            break;
        case WM_DESTROY:
            PostQuitMessage(0);
            break;
        default:
            return DefWindowProc(hwnd, msg, wParam, lParam);
    }
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCdLine, int nCMDShow)
{
    WNDCLASSEX wc;
    HWND hwnd;
    MSG msg;

    wc.cbSize = sizeof(WNDCLASSEX);
    wc.style = 0;
    wc.lpfnWndProc = WndProc;
    wc.cbClsExtra = 0;
    wc.cbWndExtra = 0;
    wc.hInstance = hInstance;
    wc.hIcon = LoadIcon(NULL, IDI_APPLICATION);
    wc.hCursor = LoadCursor(NULL, IDC_ARROW);
    wc.hbrBackground = (HBRUSH)(COLOR_WINDOW+1);
    wc.lpszMenuName = NULL;
    wc.lpszClassName = zClassName;
    wc.hIconSm = LoadIcon(NULL, IDI_APPLICATION);

    if (!RegisterClassEx(&wc)) {
        MessageBox(NULL,
            "Registro de la ventana ha fallado!!!",
            "Error fatal",
            MB_ICONEXCLAMATION | MB_OK
        );
        return 0;
    }

    hwnd = CreateWindowEx(
        WS_EX_CLIENTEDGE,
        zClassName,
        "Titulo de la ventana",
        WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, CW_USEDEFAULT, 240, 120,
        NULL, NULL, hInstance, NULL
    );

    HWND hwndButton = CreateWindow(
        "BUTTON",
        "SI",
        WS_TABSTOP | WS_VISIBLE | WS_CHILD | BS_DEFPUSHBUTTON,
        10,
        20,
        100,
        20,
        hwnd,
        NULL,
        (HINSTANCE)GetWindowLongPtr(hwnd, GWLP_HINSTANCE),
        NULL
    );

    if (hwnd == NULL) {
        MessageBox(NULL,
            "Registro de la ventana ha fallado!!!",
            "Error fatal",
            MB_ICONEXCLAMATION | MB_OK
        );
        return 0;
    }

    ShowWindow(hwnd, nCMDShow);
    UpdateWindow(hwnd);

    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return msg.wParam;
}
