defmodule Prime do
  def print_primes_up_to(n) when n > 1 do
    Enum.filter(2..n, &prime?/1) |> Enum.each(&IO.puts(&1))
  end

  def prime?(2), do: true
  def prime?(3), do: true
  def prime?(n) when rem(n, 2) == 0 or rem(n, 3) == 0, do: false
  def prime?(n) do
    limit = round(:math.sqrt(n))
    Enum.any?(5..limit, fn x -> rem(n, x) == 0 or rem(n, x + 2) == 0 end)
  end
end

Prime.print_primes_up_to(10)
