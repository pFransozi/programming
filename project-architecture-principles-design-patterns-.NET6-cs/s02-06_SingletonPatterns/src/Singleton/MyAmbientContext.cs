using System;

namespace Singleton
{
    public class MyAmbientContext
    {

        /*this is a thread-safe way to instantiate using a singleton pattern. 
        The lack of ifs avoid processor lost.*/
        public static MyAmbientContext Current { get; } = new MyAmbientContext();

        private MyAmbientContext() { }

        public void WriteSomething(string something)
        {
            Console.WriteLine($"This is your something: {something}");
        }
    }
}
