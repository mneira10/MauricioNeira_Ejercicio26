#include <iostream>
#include <fstream>
#include <ctime>
#include <chrono>
using namespace std;

main(int argc, char const *argv[])
{

  auto t1 = chrono::high_resolution_clock::now();

  if (argc < 4)
  {
    cout << "Insuficient arguments passed. Need a file to read from, a file to write the results to and a file to write the time taken to run." << endl;
  }
  else
  {

    ifstream fin;
    fin.open(argv[1], ios::in);

    int cuenta[5] = {0, 0, 0, 0, 0};

    char c;

    int cont = 0;
    fin.get(c);
    while (!fin.eof())
    {
      
      if (c - '0' == 1)
      {
        cuenta[0]++;
        cont = 1;
      }
      else
      {
        if (c - '0' == cont + 1)
        {
          cuenta[cont]++;
          cont++;
          if (cont == 5)
          {
            cont = 0;
          }
        }
        else
        {
          cont = 0;
        }
      }

      
      fin.get(c);
    }
    ofstream myfile;
    myfile.open (argv[2]);
    // myfile << "Writing this to a file.\n";
    for (int i = 0; i < (sizeof(cuenta)/sizeof(*cuenta)); i++)
    {
      myfile << cuenta[i] << endl;
    }
    myfile.close();
  }

  ofstream timeFile;
  timeFile.open (argv[3],ios_base::app);
  // time in seconds
  auto t2 = chrono::high_resolution_clock::now();
  chrono::duration<int64_t,nano> elapsed = t2 - t1;
  timeFile << elapsed.count()  <<endl;
  timeFile.close();
  return 0;
}
